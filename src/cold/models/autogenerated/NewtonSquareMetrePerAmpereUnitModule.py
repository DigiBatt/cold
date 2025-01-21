
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class NewtonSquareMetrePerAmpereUnit(SIDimensionalUnit):
    """
    Class representing the `NewtonSquareMetrePerAmpereUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_431ce3bc_3d54_481d_a10d_7c4a4418732a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NewtonSquareMetrePerAmpereUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NewtonSquareMetrePerAmpereUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_431ce3bc_3d54_481d_a10d_7c4a4418732a',
    
    class_name='NewtonSquareMetrePerAmpereUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_431ce3bc_3d54_481d_a10d_7c4a4418732a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NewtonSquareMetrePerAmpereUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    