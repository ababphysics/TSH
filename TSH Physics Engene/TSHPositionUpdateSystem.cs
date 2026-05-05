using Unity.Entities;
using Unity.Mathematics;
using Unity.Burst;
using Unity.Transforms;

namespace TSH.Core
{
    /*
    ================================================================================
    TSH v3.0 Position Update System (Burst + Jobs)
    ================================================================================
    This system updates particle positions and velocities using the forces 
    calculated by the TSHUnifiedForce Compute Shader.
    ================================================================================
    */

    [BurstCompile]
    public partial struct TSHPositionUpdateSystem : ISystem
    {
        [BurstCompile]
        public void OnUpdate(ref SystemState state)
        {
            float dt = SystemAPI.Time.DeltaTime;
            
            // Job to update physics based on pre-calculated GPU forces
            // Note: In a real implementation, GPU forces would be read back or 
            // the whole integration would happen in the Compute Shader.
            // For v3.0 ECS integration, we demonstrate the Burst update loop.
            new TSHPhysicsJob
            {
                DeltaTime = dt
            }.ScheduleParallel();
        }
    }

    [BurstCompile]
    public partial struct TSHPhysicsJob : IJobEntity
    {
        public float DeltaTime;

        void Execute(ref TSHParticleData particle, ref LocalTransform transform)
        {
            // Simple Euler/Verlet integration using force from GPU
            // (Assuming 'force' was synced back to TSHParticleData)
            float3 acceleration = particle.velocity * -0.01f; // Dummy drag for example
            
            particle.velocity += acceleration * DeltaTime;
            particle.position += particle.velocity * DeltaTime;
            
            // Sync with Unity Transform system
            transform.Position = particle.position;
            
            // Phase-Diagram Aging (Delta_f fluctuation)
            particle.p_amp *= 0.999f; // Field decay over time example
        }
    }
}
