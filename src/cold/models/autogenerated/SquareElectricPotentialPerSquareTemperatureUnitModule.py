
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class SquareElectricPotentialPerSquareTemperatureUnit(SIDimensionalUnit):
    """
    Class representing the `SquareElectricPotentialPerSquareTemperatureUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_58c5b65c_c896_4740_80d9_ff9a7643c7e8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareElectricPotentialPerSquareTemperatureUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareElectricPotentialPerSquareTemperatureUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_58c5b65c_c896_4740_80d9_ff9a7643c7e8',
    
    class_name='SquareElectricPotentialPerSquareTemperatureUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_58c5b65c_c896_4740_80d9_ff9a7643c7e8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SquareElectricPotentialPerSquareTemperatureUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    