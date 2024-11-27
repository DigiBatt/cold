customizations = {
    "EMMO": {
        "imports": [ ],
        "properties": [
            {"name": "extra_property", "range": "str", "alias": "extraProperty", "default": "None"}
        ],
        "methods": [
            """
def custom_method(self):
    return f"Custom method in {self.__class__.__name__}"
"""
        ]
    },
    "ElectrochemicalDevice": {
        "properties": [
            {"name": "custom_feature", "range": "str", "alias": "customFeature"}
        ]
    },
    "MeasurementUnit": {
        "imports": [
            "import importlib"
        ],
        "methods": [
            """
    @classmethod
    def from_class_name(cls, unit: str):
        \"\"\"Dynamically instantiate the correct subclass of MeasurementUnit.\"\"\"
        try:
            # Dynamically import the module based on the unit name
            module_name = f"{unit}Module"  # Assumes module naming convention matches
            module = importlib.import_module(f".{module_name}", package=cls.__module__.rsplit('.', 1)[0])

            # Get the class from the module
            unit_class = getattr(module, unit)

            # Instantiate and return the class
            return unit_class()
        except (ModuleNotFoundError, AttributeError) as e:
            raise ValueError(f"Unit '{unit}' is not defined or cannot be loaded.") from e
"""
        ]
    },
    "Property": {
        "imports": [],
        "properties": [
            {"name": "hasNumericalPart", "range": "NumericalPart", "alias": "hasNumericalPart"},
            {"name": "hasMeasurementUnit", "range": "MeasurementUnit", "alias": "hasMeasurementUnit"}
        ],
        "methods": [
            """
    def __init__(self, value: float, unit: str, **kwargs):
        \"\"\"Override __init__ for simplified instantiation.\"\"\" 
        # Dynamically create a MeasurementUnit instance 
        unit_instance = MeasurementUnit.from_class_name(unit) 
        super().__init__(
            hasNumericalPart=NumericalPart(hasNumericalValue=value),
            hasMeasurementUnit=unit_instance,
            **kwargs,
        )
"""
        ]
    },
}
