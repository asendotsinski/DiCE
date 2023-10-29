from dice_ml.explainer_interfaces.explainer_base import ExplainerBase

class LinearDependencyWrapper(ExplainerBase):
    def  __init__(self, gradient_explainer, *args, **kwargs):
        self.gradient_explainer = gradient_explainer(*args, **kwargs)

        # forward all inherited methods from ExplainerBase to the wrapped class
        for methodname in [method for method in dir(ExplainerBase) if (method[0:2] != "__")]:
            setattr(self, methodname, getattr(self.gradient_explainer, methodname))

    def __getattr__(self, attribute):
        return getattr(self.gradient_explainer, attribute)

    def test(self, name='user'):
        print(f"This works, {name}!")

