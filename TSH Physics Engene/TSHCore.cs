using Unity.Entities;
using Unity.Mathematics;
using UnityEngine;

namespace TSH.Core
{
    /*
    ================================================================================
    TSH Physics Engine v1.0 (Official Release)
    ================================================================================
    Master Core definitions for the Grand Unified Universal OS.
    ================================================================================
    */

    public struct MaterialCoeffs
    {
        public float4 beta; // q1:EM, q2:Strong, q3:Weak, q4:Custom
        public float alpha; // Structural Tension
        public float strongThreshold;
        public float coreThreshold;
    }

    public struct TSHParticleData : IComponentData
    {
        public float3 position;
        public float3 velocity;
        public float mass;
        public float p_amp;
        public float sigma;
        public float4 charges;
        public int phase;
        public int materialId;
    }

    [CreateAssetMenu(fileName = "TSHMaterial", menuName = "TSH/Unified Material v1.0")]
    public class TSHMaterialAsset : ScriptableObject
    {
        public string materialName;
        public int materialId;
        
        [Header("Coupling Constants (Beta)")]
        public float q1_EM = 40f;
        public float q2_Strong = 180f;
        public float q3_Weak = 20f;
        public float q4_Custom = 0f;

        [Header("Structural (Alpha)")]
        public float alpha = 13.5f;

        public MaterialCoeffs ToCoeffs()
        {
            return new MaterialCoeffs
            {
                beta = new float4(q1_EM, q2_Strong, q3_Weak, q4_Custom),
                alpha = alpha,
                strongThreshold = alpha * 1.5f,
                coreThreshold = alpha * 3.0f
            };
        }
    }
}
