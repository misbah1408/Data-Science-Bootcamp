## 📘 **Topic 6: Performance Metrics in Regression**

---

After training a regression model, you need to **measure how well it performs** on data.

We use **performance metrics** to:

* Quantify error
* Compare models
* Guide improvements

---

### 📊 Common Regression Metrics:

| Metric   | Meaning                      | Good When...                             |
| -------- | ---------------------------- | ---------------------------------------- |
| **MSE**  | Mean Squared Error           | You want to penalize large errors        |
| **MAE**  | Mean Absolute Error          | You want to treat all errors equally     |
| **RMSE** | Root Mean Squared Error      | Like MSE, but in original units          |
| **R²**   | Coefficient of Determination | You want to know % of variance explained |

Let’s go through each:

---

## 1️⃣ **Mean Squared Error (MSE)**

$$
MSE = \frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2
$$

* **Penalizes larger errors** more heavily.
* Always positive.
* Units are **squared** (e.g., dollars²).

---

## 2️⃣ **Mean Absolute Error (MAE)**

$$
MAE = \frac{1}{n} \sum_{i=1}^{n} |Y_i - \hat{Y}_i|
$$

* Simpler than MSE.
* Treats all errors **equally**.
* Same unit as target variable.

---

## 3️⃣ **Root Mean Squared Error (RMSE)**

$$
RMSE = \sqrt{MSE}
$$

* Gives error in **same units** as the output.
* Easier to interpret than MSE.

---

## 4️⃣ **R² Score (Coefficient of Determination)**

$$
R^2 = 1 - \frac{\sum (Y - \hat{Y})^2}{\sum (Y - \bar{Y})^2}
$$

* Measures **how well the model explains variance** in data.
* Ranges from:

  * **1** (perfect model)
  * **0** (no better than mean)
  * **Negative** (worse than mean)

---

## 🧪 Python Example:

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Actual and Predicted
Y_true = np.array([40000, 50000, 60000, 70000])
Y_pred = np.array([39000, 51000, 61000, 69000])

# Metrics
mse = mean_squared_error(Y_true, Y_pred)
mae = mean_absolute_error(Y_true, Y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y_true, Y_pred)

print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("R² Score:", r2)
```

---

## 🎯 Which one to use?

| Use Case                      | Metric     |
| ----------------------------- | ---------- |
| Want to penalize big errors   | MSE / RMSE |
| Want interpretability         | MAE / RMSE |
| Want to compare model quality | R²         |

---

### ✅ Summary:

* Use **MSE/RMSE** for penalty-based models (like gradient descent)
* Use **MAE** for simple interpretability
* Use **R²** to measure how well your model captures trends