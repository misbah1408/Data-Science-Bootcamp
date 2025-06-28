## 📘 **Topic 2: Cost Function in Linear Regression**

---

### 🧠 **Why do we need a Cost Function?**

When we draw a line like:

$$
\hat{Y} = mX + b
$$

We need to know **how good or bad** this line is at predicting the real Y values.

> The **Cost Function** tells us **how far off** our predictions are from the actual data.

---

### 🎯 **Goal** of Cost Function:

Minimize the error between actual and predicted values.

---

### 📐 **Most Common Cost Function**:

### **Mean Squared Error (MSE)**

$$
J(m, b) = \frac{1}{n} \sum_{i=1}^{n} (\hat{Y}_i - Y_i)^2
$$

Where:

* $J$ is the cost
* $\hat{Y}_i$ = predicted value = $mX_i + b$
* $Y_i$ = actual value
* $n$ = number of data points

---

### 🔍 Intuition:

For each data point:

* Compute the **difference** between predicted and actual values.
* **Square it** (to remove negative signs and penalize larger errors).
* **Average** all squared differences.

---

### 🔢 **Example** (Manually):

Let's say:

| X | Y (Actual) | $\hat{Y}$ (Predicted) |
| - | ---------- | --------------------- |
| 1 | 40000      | 41000                 |
| 2 | 50000      | 49000                 |

$$
\text{MSE} = \frac{1}{2} \left[(41000 - 40000)^2 + (49000 - 50000)^2 \right] = \frac{1}{2} \left[1000^2 + (-1000)^2 \right] = \frac{1}{2} (1,000,000 + 1,000,000) = 1,000,000
$$

---

### ✅ **In Python (MSE using NumPy)**

```python
import numpy as np

# Actual and Predicted values
Y = np.array([40000, 50000])
Y_pred = np.array([41000, 49000])

# Mean Squared Error
mse = np.mean((Y - Y_pred)**2)
print("MSE:", mse)
```

---

### ❗ Why is minimizing cost important?

Because the lower the cost, the **closer our model is to the real data** — and that’s what training is all about: **minimizing this cost** by adjusting `m` and `b`.
