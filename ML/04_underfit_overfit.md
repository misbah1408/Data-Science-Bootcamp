## 📘 **Topic 7: Overfitting and Underfitting**

---

This is one of the **most important concepts** in machine learning. It helps you understand whether your model is **too simple**, **too complex**, or **just right**.

---

## 🧠 Definitions:

### ✅ **Underfitting**:

* Model is **too simple** to learn the data well.
* **High bias**, low variance.
* Happens when:

  * You use a linear model for curved data
  * Not enough training
  * Important features are missing

📉 **Symptoms**:

* **High error** on training set **and** test set
* The model doesn’t even fit the training data properly

---

### ❌ **Overfitting**:

* Model is **too complex**, learning noise instead of patterns.
* **Low bias**, high variance.
* Happens when:

  * Too many features
  * Too complex a model (e.g., high-degree polynomial)
  * Small dataset

📉 **Symptoms**:

* **Low training error**, **high test error**
* The model fits training data perfectly but performs poorly on new data

---

### 📊 Visual Example:

| Model Type   | Train Error | Test Error |
| ------------ | ----------- | ---------- |
| Underfitting | High        | High       |
| Good Fit     | Low         | Low        |
| Overfitting  | Very Low    | High       |

---

## 🔧 How to Fix Each Problem:

### 🔄 **Fixing Underfitting**:

* Use a **more complex model**
* Add more **features**
* Train for more **epochs**
* Reduce **regularization**

---

### 🛠️ **Fixing Overfitting**:

* Use a **simpler model**
* **Reduce features**
* **Add more training data**
* Use **regularization** (e.g., L1/L2)
* Apply **cross-validation**

---

## 🧪 Python Check: Train vs Test Error

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Example Data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([3, 6, 9, 12, 15, 18, 21, 24])  # Perfectly linear

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

print("Train MSE:", train_mse)
print("Test MSE:", test_mse)
```

* If **Train MSE ≈ Test MSE** → Good Fit
* If **Train MSE ≪ Test MSE** → Overfitting
* If **Both MSEs are high** → Underfitting

---

## ✅ Summary:

* Underfitting = too simple, learns nothing useful
* Overfitting = too complex, memorizes instead of learning
* Aim for **generalization**: low train **and** test error