import matplotlib.pyplot as plt
import numpy as np

def plot():
        # --- Sample Data ---
        months = np.arange(1, 13)
        month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        product_a_sales = [1200, 1350, 1100, 1500, 1800, 2100,
                        2300, 2250, 1950, 1700, 1600, 2400]

        product_b_sales = [800, 850, 900, 1000, 1100, 1050,
                        1200, 1300, 1250, 1150, 1400, 1600]

        # --- Create the Plot ---
        fig, ax = plt.subplots(figsize=(12, 6))

        ax.plot(months, product_a_sales, marker="o", linewidth=2.5,
                color="#2196F3", label="Product A", markersize=7)

        ax.plot(months, product_b_sales, marker="s", linewidth=2.5,
                color="#FF5722", label="Product B", markersize=7, linestyle="--")

        # --- Fill area under the lines for visual appeal ---
        ax.fill_between(months, product_a_sales, alpha=0.08, color="#2196F3")
        ax.fill_between(months, product_b_sales, alpha=0.08, color="#FF5722")

        # --- Labels & Title ---
        ax.set_title("Monthly Sales Performance: Product A vs Product B (2024)",
                fontsize=16, fontweight="bold", pad=15)
        ax.set_xlabel("Month", fontsize=13, labelpad=10)
        ax.set_ylabel("Units Sold", fontsize=13, labelpad=10)

        # --- X-axis tick labels ---
        ax.set_xticks(months)
        ax.set_xticklabels(month_labels, fontsize=11)
        ax.set_yticks(range(600, 2800, 200))

        # --- Grid ---
        ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.7, color="gray")
        ax.set_axisbelow(True)  # Grid lines behind data

        # --- Legend ---
        ax.legend(fontsize=12, loc="upper left", framealpha=0.9, shadow=True)

        # --- Annotations for peak values ---
        peak_a = max(product_a_sales)
        peak_b = max(product_b_sales)
        ax.annotate(f"Peak: {peak_a}", xy=(12, peak_a), xytext=(10.5, peak_a + 100),
                fontsize=9, color="#2196F3",
                arrowprops=dict(arrowstyle="->", color="#2196F3", lw=1.2))
        ax.annotate(f"Peak: {peak_b}", xy=(12, peak_b), xytext=(10.2, peak_b + 100),
                fontsize=9, color="#FF5722",
                arrowprops=dict(arrowstyle="->", color="#FF5722", lw=1.2))

        plt.tight_layout()
        plt.show()

plot()
