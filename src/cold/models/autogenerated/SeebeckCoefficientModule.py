
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity





from .MeasurementUnitModule import MeasurementUnit





class SeebeckCoefficient(ISQDerivedQuantity, CondensedMatterPhysicsQuantity):
    """
    Class representing the `SeebeckCoefficient` entity, which inherits from:
    - ISQDerivedQuantity, CondensedMatterPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b725aad8_55e2_430a_b2d2_f84b8333484e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SeebeckCoefficient'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SeebeckCoefficient(
    
    class_iri='https://w3id.org/emmo#EMMO_b725aad8_55e2_430a_b2d2_f84b8333484e',
    
    class_name='SeebeckCoefficient',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    hasMeasurementUnit="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b725aad8_55e2_430a_b2d2_f84b8333484e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SeebeckCoefficient',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
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
    
    

    

    