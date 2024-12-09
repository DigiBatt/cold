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
    "Electrode": {
        "properties": [
            {"name": "hasCoating", "range": "Coating", "alias": "hasCoating"},
            {"name": "hasCurrentCollector", "range": "CurrentCollector", "alias": "hasCurrentCollector"}
        ]
    },
    "ElectrochemicalCell": {
        "properties": [
            {"name": "hasPositiveElectrode", "range": "Electrode", "alias": "hasPositiveElectrode"},
            {"name": "hasNegativeElectrode", "range": "Electrode", "alias": "hasNegativeElectrode"}
        ]
    },
    "CR2032": {
        "imports": [
            "from .DiameterModule import Diameter",
            "from .ThicknessModule import Thickness"
        ],
        "instantiated_defaults": [
            "hasNegativeElectrode",
            "hasPositiveElectrode",
            "hasCase",
            "hasElectrolyte"
        ],
        "methods": [
            """
    @root_validator(pre=True)
        def set_defaults(cls, values):
            values["hasNegativeElectrode"] = values.get("hasNegativeElectrode", LithiumElectrode())
            values["hasPositiveElectrode"] = values.get("hasPositiveElectrode", ManganeseDioxideElectrode())
            values["hasProperty"] = values.get("hasProperty", [
                Diameter(0.020, "Metre"),
                Thickness(0.0032, "Metre")
            ])

            return values
"""
        ]
    }
}