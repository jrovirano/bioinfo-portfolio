import pandas as pd
import matplotlib.pyplot as plt

# Example dataset
data = pd.DataFrame({
    "gene": ["A", "B", "C", "D"],
    "expression": [10, 50, 30, 20]
})

print(data)

plt.bar(data["gene"], data["expression"])
plt.title("Gene Expression")
plt.xlabel("Gene")
plt.ylabel("Expression")
plt.show()
