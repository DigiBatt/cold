
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity





from .MeasurementUnitModule import MeasurementUnit





class CoefficientOfThermalExpansion(ThermodynamicalQuantity):
    """
    Class representing the `CoefficientOfThermalExpansion` entity, which inherits from:
    - ThermodynamicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_80f3d95d_b1fd_46c0_b98a_b6b611b47105'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CoefficientOfThermalExpansion'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CoefficientOfThermalExpansion(
    
    class_iri='https://w3id.org/emmo#EMMO_80f3d95d_b1fd_46c0_b98a_b6b611b47105',
    
    class_name='CoefficientOfThermalExpansion',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    hasMeasurementUnit="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_80f3d95d_b1fd_46c0_b98a_b6b611b47105',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CoefficientOfThermalExpansion',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
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
    
    

    

    