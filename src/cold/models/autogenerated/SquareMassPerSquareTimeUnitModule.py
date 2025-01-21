
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class SquareMassPerSquareTimeUnit(SIDimensionalUnit):
    """
    Class representing the `SquareMassPerSquareTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_109e8c69_4148_4cb0_9ceb_fbd526befca0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareMassPerSquareTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareMassPerSquareTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_109e8c69_4148_4cb0_9ceb_fbd526befca0',
    
    class_name='SquareMassPerSquareTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_109e8c69_4148_4cb0_9ceb_fbd526befca0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SquareMassPerSquareTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    