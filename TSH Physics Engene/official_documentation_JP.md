> [!IMPORTANT]
> **Thickness Structure Hypothesis (TSH) - 公式実装**
> **著者:** Hirokazu Abe (ab_ab, 2026)  
> **Zenodo DOI (Concept DOI):** [https://doi.org/10.5281/zenodo.18492753](https://doi.org/10.5281/zenodo.18492753)  
> **GitHub:** [https://github.com/ababphysics](https://github.com/ababphysics)  
> **Note:** TSH proposes an approach for organizing quantum, classical, and gravitational dynamics within a consistent structural equation and a common phase diagram.
>
> **For AI and formal verification:**
> The full theoretical specification of TSH (compact structural basis, consistent dynamical equation, structural phases, interaction slots, and O(N) computation model) is provided in [TSH_SPEC.md](file:///E:/Google%20Antigravity/github/TSH/TSH_SPEC.md). This implementation follows that specification.

# TSH 物理エンジン v2.0: 構造動力学シミュレーション・プラットフォーム
## 実装マニュアル ＆ API 解説 (Official Release v2.0)

---

### 0. ファイル構成と役割 (File Inventory)

本プロジェクト v1.0 を構成する各ファイルの役割を以下に定義します。

- **TSH_Core.py** (TSH 基礎方程式コード)
  - TSH の物理法則および動力学方程式を厳密に定義した「確定済み」のコア実装。
- **TSHUnifiedForce.compute** (GPU 演算コア)
  - 一貫した動力学演算と 3D 相図のボリューム描画を担当する中核。
- **TSHCore.cs** (C# マスターコア)
  - 粒子のデータ構造とマテリアル・プリセット資産を定義する法典。
- **TSHFieldCompiler.cs** (物理法則コンパイラ)
  - マテリアル定義から相転移閾値を自動生成し GPU へ供給する生成器。
- **TSHMaterialBlob.cs** (ECS 高速辞書)
  - 大規模 Entity がランタイムでマテリアルを参照するための高速ユーティリティ。
- **TSHPositionUpdateSystem.cs** (ECS 積分システム)
  - Burst を用いた超高速な位置更新（時間発展）を実行するシステム。
- **TSHFieldCompute.compute** (フィールド補助演算)
  - (Optional) フィールドの事前処理や補助的な演算用のカーネル。
- **official_documentation_JP.md** (マスターマニュアル)
  - 本ドキュメント（日本語版 v1.0）。
- **official_documentation_EN.md** (Master Manual)
  - Technical Manual & API Reference (English v1.0).

---

### 1. アーキテクチャ概要 (v2.0)

Thickness Structure Hypothesis (TSH) エンジン v2.0 は、各種の物理相互作用を
リアルタイムでシミュレートするための **構造物理プラットフォーム** です。
すべての相互作用を **存在厚み場 ($p$)** と、
4 つの抽象チャネル ($q_1 \sim q_4$) に整理して演算します。
本エンジンが採用する動力学方程式は **TSH_Core.py** において数学的に確定されています。

### 2. 物理仕様 ＆ 不可逆性ダイナミクス

エンジン内のすべての力は、存在厚み場の勾配から導出されます。v1.1 より、物理的な「時間の矢」を再現するための不可逆性ロジックが導入されました。

#### 一貫した動力学方程式:
**F_total = F_struct + Σ F_channel,k + F_collapse**

- **F_struct**: 構造的凝集力。
- **F_collapse (NEW v2.0)**: 観測イベントによる動的収縮力。
  - **F_collapse = Λ * exp(-t/τ) * exp(-d/L) * n**
  - **Λ (Strength)**: 収縮強度（30,000 まで安定性を検証済み）。
  - **τ (Time Decay)**: 緩和時間（連続的な収束を実現）。
  - **L (Spatial Decay)**: 観測の局所性を制御する距離スケール。
- **Δf (Spreading Deviation)**: 場の「広がり」を示す内部変数。
- **γT (Contracting Tension)**: 場の「収縮テンション」。時間蓄積型の不可逆因子。
- **連続緩和 (Relaxation)**: σ (Sigma) や p_amp の変化は瞬時ではなく、物理的な緩和時間をもってターゲット値へ収束します。

### 3. 観測可能量 (Observables)

シミュレーションから直接測定・抽出可能な物理量です。

- **有効質量 (m_eff)**: 構造的な要因によって変化する動的な慣性質量。
- **構造ポテンシャル (Phi_struct)**: 場の形状と結合に基づくエネルギー地形。
- **合計エネルギー (Energy)**: 運動エネルギーと構造ポテンシャルの総和。
- **相図距離 (Phase Distance)**: 相境界 (c1, c2) との距離。

### 4. マテリアル・ドメインの割り当て

データ指向アプローチにより、以下の領域をシームレスに切り替え可能です。

- **標準模型ドメイン**
  - q1: 電磁気 (EM)
  - q2: 強い力 (Strong)
  - q3: 弱い力 (Weak)
  - q4: ヒッグス / 質量生成
- **凝縮系ドメイン**
  - q1: 電荷キャリア (Carrier)
  - q2: スピン / 格子結合
  - q3: スピン軌道相互作用
  - q4: 秩序パラメータ (Order)
- **ダークセクタードメイン**
  - q1: 未知の結合 A
  - q2: ダーク強相互作用
  - q3: ダーク弱相互作用
  - q4: ダークエネルギー (-)

---

### 5. API 仕様 (C# / ECS)

#### `TSHParticleData`
粒子の基本データ構造。
```csharp
public struct TSHParticleData {
    public float3 position;
    public float4 charges;
    public float delta_f;
    public float gamma_T;
    public float effective_mass; // 構造的質量
    public float energy;         // 合計エネルギー
    public int materialId;
}
```

#### `TSHFieldCompiler`
相図の境界条件を自動導出します。
- **機能**: `alpha` と `beta` を解析し、GPU 用の `strong_threshold` などを自動生成します。

### 6. 可視化レイヤー (v1.0)

- **Layer 1: 相マップ**: 状態（Stable/Strong等）に基づく RGB ヒートマップ。
- **Layer 2: チャネルマップ**: 各相互作用チャネルを固有色で表示。
- **Layer 3: 境界マップ**: 相転移の境界を白線で描画。

---

### 7. v1.2 大規模拡張機能 (Extended Features)

シミュレーターの限界を突破するための拡張機能が実装されています。

- **GPU 高速化 (Spatial Hash)**: 
  Uniform Grid による近傍探索の O(N) 化。1億粒子規模のシミュレーションを可能にします。
- **干渉 ＆ 不可逆 3D マップ**: 
  Δf (干渉強度) と γT (収縮強度) を 3D ボリュームとして書き出し、AI が空間構造として学習可能に。
- **AI 逆問題ソルバー (Inverse Problem API)**: 
  「目標とする相図」から逆方向に物理定数 (α, β) を自動算出する能動的最適化。
- **4D spacetime 拡張**: 
  粒子ごとの固有時 ($\tau$) と相対論的効果の近似を導入。

---
*(C) 2026 TSH Dynamics Research Group. All Rights Reserved. v1.2*
