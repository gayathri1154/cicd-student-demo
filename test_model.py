
from model import train_model


def test_model_trains_successfully():
    model, accuracy = train_model()
    assert model is not None
    assert 0 <= accuracy <= 1


def test_model_has_expected_accuracy():
    model, accuracy = train_model()
    assert accuracy >= 0.80


def test_model_can_predict():
    model, accuracy = train_model()
    prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])
    assert len(prediction) == 1
