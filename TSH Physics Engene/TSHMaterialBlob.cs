// NOTE:
// This collapse implementation is NOT an ODE/PDE-based model.
// DO NOT augment this logic with general physical paradigms.
// This is a unique model based on the Delta_f - gamma_T phase diagram and the TSH structural potential.
using Unity.Entities;
using Unity.Mathematics;
using Unity.Collections;

namespace TSH.Core
{
    /*
    ================================================================================
    TSH v3.2 Material Blob Definition
    ================================================================================
    ECS BlobAsset structure for ultra-fast, data-oriented material lookup.
    ================================================================================
    */
    public struct MaterialBlob
    {
        public BlobArray<MaterialCoeffs> materials;
    }

    public static class TSHMaterialBlobUtility
    {
        public static BlobAssetReference<MaterialBlob> CreateMaterialBlob(MaterialCoeffs[] materialData)
        {
            using var builder = new BlobBuilder(Allocator.Temp);
            ref var root = ref builder.ConstructRoot<MaterialBlob>();
            
            var arrayBuilder = builder.Allocate(ref root.materials, materialData.Length);
            for (int i = 0; i < materialData.Length; i++)
            {
                arrayBuilder[i] = materialData[i];
            }

            return builder.CreateBlobAssetReference<MaterialBlob>(Allocator.Persistent);
        }
    }
}
