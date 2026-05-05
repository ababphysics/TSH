# TSH 物理エンジン v1.0: 万物の理論を記述する Universal OS
## 実装マニュアル ＆ API 解説 (Official Release v1.0)

---

### 0. ファイル構成と役割 (File Inventory)

本プロジェクト v1.0 を構成する各ファイルの役割を以下に定義します。

- **ultimate_tsh_simulator.py** (物理リファレンス)
  - Python によるプロトタイプ。v1.0 における物理ロジックの正解コードです。
- **TSHUnifiedForce.compute** (GPU 演算コア)
  - v1.0 統一動力学演算と 3D 相図のボリューム描画を担当する中核。
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

### 1. アーキテクチャ概要 (v1.0)

TSH (Thickness Structure Hypothesis) エンジン v1.0 は、任意の物理相互作用を
リアルタイムでシミュレートするための **統合場物理プラットフォーム** です。
すべての基本相互作用を単一の **存在厚み場 ($p$)** と、
4 つの抽象チャネル ($q_1 \sim q_4$) に集約して演算します。

### 2. 物理仕様

エンジン内のすべての力は、存在厚み場の勾配から導出されます。

#### 統合動力学方程式:
**F_total = F_struct + Σ F_channel,k**

- **F_struct**: 構造的凝集力。場の勾配による安定性を維持します。
- **F_channel,k**: 相互作用ダイナミクス。チャネルごとのチャージと結合定数に基づく力。

### 3. マテリアル・ドメインの割り当て

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

### 4. API 仕様 (C# / ECS)

#### `TSHParticleData`
粒子の基本データ構造。
```csharp
public struct TSHParticleData {
    public float3 position;
    public float4 charges; // 抽象チャネル q1-q4
    public int materialId; // マテリアル設定のインデックス
}
```

#### `TSHFieldCompiler`
相図の境界条件を自動導出します。
- **機能**: `alpha` と `beta` を解析し、GPU 用の `strong_threshold` などを自動生成します。

### 5. 可視化レイヤー (v1.0)

- **Layer 1: 相マップ**: 状態（Stable/Strong等）に基づく RGB ヒートマップ。
- **Layer 2: チャネルマップ**: 各相互作用チャネルを固有色で表示。
- **Layer 3: 境界マップ**: 相転移の境界を白線で描画。

---
*(C) 2026 TSH Dynamics Research Group. All Rights Reserved. v1.0*
