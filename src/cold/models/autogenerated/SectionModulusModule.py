
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity



from .MechanicalQuantityModule import MechanicalQuantity





from .MeasurementUnitModule import MeasurementUnit





class SectionModulus(ISQDerivedQuantity, MechanicalQuantity):
    """
    Class representing the `SectionModulus` entity, which inherits from:
    - ISQDerivedQuantity, MechanicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_26b13395_0031_4da2_b4d0_55eca1792107'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SectionModulus'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SectionModulus(
    
    class_iri='https://w3id.org/emmo#EMMO_26b13395_0031_4da2_b4d0_55eca1792107',
    
    class_name='SectionModulus',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    hasMeasurementUnit="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_26b13395_0031_4da2_b4d0_55eca1792107',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SectionModulus',
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
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    
    hasMeasurementUnit: Optional[MeasurementUnit] = Field(
        None,
        alias="hasMeasurementUnit"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    @validator("hasMeasurementUnit", pre=True, always=True)
    def validate_hasMeasurementUnit(cls, value):
        if value is not None and not isinstance(value, MeasurementUnit):
            raise ValueError(f"Field 'hasMeasurementUnit' must be an instance of 'MeasurementUnit' or its subclass.")
        return value
    
    

    

    