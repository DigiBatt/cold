
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class MassPerQuarticLengthTimeUnit(SIDimensionalUnit):
    """
    Class representing the `MassPerQuarticLengthTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9cffc70d_4b60_4187_a7cd_706f5740ae87'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassPerQuarticLengthTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassPerQuarticLengthTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_9cffc70d_4b60_4187_a7cd_706f5740ae87',
    
    class_name='MassPerQuarticLengthTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9cffc70d_4b60_4187_a7cd_706f5740ae87',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassPerQuarticLengthTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    