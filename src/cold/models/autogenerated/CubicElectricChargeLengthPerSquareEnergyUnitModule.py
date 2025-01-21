
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class CubicElectricChargeLengthPerSquareEnergyUnit(SIDimensionalUnit):
    """
    Class representing the `CubicElectricChargeLengthPerSquareEnergyUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_360adeca_9eee_4bb9_a5ca_728756c1ed4a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CubicElectricChargeLengthPerSquareEnergyUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CubicElectricChargeLengthPerSquareEnergyUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_360adeca_9eee_4bb9_a5ca_728756c1ed4a',
    
    class_name='CubicElectricChargeLengthPerSquareEnergyUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_360adeca_9eee_4bb9_a5ca_728756c1ed4a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CubicElectricChargeLengthPerSquareEnergyUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    