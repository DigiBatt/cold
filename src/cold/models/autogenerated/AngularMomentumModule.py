
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity



from .MechanicalQuantityModule import MechanicalQuantity





from .MeasurementUnitModule import MeasurementUnit





class AngularMomentum(ISQDerivedQuantity, MechanicalQuantity):
    """
    Class representing the `AngularMomentum` entity, which inherits from:
    - ISQDerivedQuantity, MechanicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_66d01570_36dd_42fd_844d_29b81b029cd5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AngularMomentum'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AngularMomentum(
    
    class_iri='https://w3id.org/emmo#EMMO_66d01570_36dd_42fd_844d_29b81b029cd5',
    
    class_name='AngularMomentum',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    ISO80000Reference="example_value",
    
    hasMeasurementUnit="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_66d01570_36dd_42fd_844d_29b81b029cd5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AngularMomentum',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    
    hasMeasurementUnit: Optional[MeasurementUnit] = Field(
        None,
        alias="hasMeasurementUnit"
    )
    

    
    @validator("hasMeasurementUnit", pre=True, always=True)
    def validate_hasMeasurementUnit(cls, value):
        if value is not None and not isinstance(value, MeasurementUnit):
            raise ValueError(f"Field 'hasMeasurementUnit' must be an instance of 'MeasurementUnit' or its subclass.")
        return value
    
    

    

    