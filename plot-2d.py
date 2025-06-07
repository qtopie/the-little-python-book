import pandas as pd
import plotly.express as px

# 原始数据重构
df = pd.DataFrame([
    ["2024/7/16", None, None, 8371.7, None, None],
    ["2024/8/21", None, 2507.5, None, None, None],
    ["2024/10/24", None, None, 8006.9, None, None]
], columns=["month", "store1", "store2", "store3",
            "store4", "store5"])

# 数据重塑为长格式，便于绘图
df_long = df.melt(id_vars="month", var_name="store", value_name="amount")

# 创建动态图表，使用spline曲线，带有标记点
fig = px.line(
    df_long,
    x="month",
    y="amount",
    color="store",
    line_shape="spline",
    markers=True,
    title="各品牌资金获取趋势分析",
    labels={"amount": "USD Amount", "month": "Transaction Month"},
    hover_data={"amount": ":.2f"},
    text="amount"  # 在点上显示金额
)

# 加粗折线并连接缺失点，并设置文本显示位置
fig.update_traces(line=dict(width=6), connectgaps=True, textposition="top center")

# 增强可视化配置：旋转x轴标签、设置y轴前缀、统一悬浮提示、调整图例位置
fig.update_layout(
    xaxis=dict(tickangle=45, type='category'),
    yaxis=dict(tickprefix="$", hoverformat="$,.2f"),
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02)
)

# 展示图表
fig.show()

