
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity



from .ElectromagneticQuantityModule import ElectromagneticQuantity





from .MeasurementUnitModule import MeasurementUnit





class Permeance(ISQDerivedQuantity, ElectromagneticQuantity):
    """
    Class representing the `Permeance` entity, which inherits from:
    - ISQDerivedQuantity, ElectromagneticQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e0feea8c_318e_4dcf_92f0_751e228ed99d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Permeance'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Permeance(
    
    class_iri='https://w3id.org/emmo#EMMO_e0feea8c_318e_4dcf_92f0_751e228ed99d',
    
    class_name='Permeance',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    hasMeasurementUnit="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e0feea8c_318e_4dcf_92f0_751e228ed99d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Permeance',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    @validator("hasMeasurementUnit", pre=True, always=True)
    def validate_hasMeasurementUnit(cls, value):
        if value is not None and not isinstance(value, MeasurementUnit):
            raise ValueError(f"Field 'hasMeasurementUnit' must be an instance of 'MeasurementUnit' or its subclass.")
        return value
    
    

    

    