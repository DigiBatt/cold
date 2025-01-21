
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class TemperaturePerMagneticFluxDensityUnit(SIDimensionalUnit):
    """
    Class representing the `TemperaturePerMagneticFluxDensityUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f6fac54d_6b6d_4255_b217_4363a83f1834'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemperaturePerMagneticFluxDensityUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemperaturePerMagneticFluxDensityUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_f6fac54d_6b6d_4255_b217_4363a83f1834',
    
    class_name='TemperaturePerMagneticFluxDensityUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f6fac54d_6b6d_4255_b217_4363a83f1834',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemperaturePerMagneticFluxDensityUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    