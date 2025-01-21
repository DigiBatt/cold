
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetrologicalReferenceModule import MetrologicalReference






import importlib


class MeasurementUnit(MetrologicalReference):
    """
    Class representing the `MeasurementUnit` entity, which inherits from:
    - MetrologicalReference

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b081b346_7279_46ef_9a3d_2c088fcd79f4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeasurementUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MeasurementUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_b081b346_7279_46ef_9a3d_2c088fcd79f4',
    
    class_name='MeasurementUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    VIMTerm="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b081b346_7279_46ef_9a3d_2c088fcd79f4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeasurementUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    
    
    
    @classmethod
    def from_class_name(cls, unit: str):
        """Dynamically instantiate the correct subclass of MeasurementUnit."""
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

    
    

    