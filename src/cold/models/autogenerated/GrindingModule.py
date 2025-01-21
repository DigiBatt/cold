
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UndefinedEdgeCuttingModule import UndefinedEdgeCutting







class Grinding(UndefinedEdgeCutting):
    """
    Class representing the `Grinding` entity, which inherits from:
    - UndefinedEdgeCutting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2138677c_845a_4bc2_8be7_7b0a07b4777d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Grinding'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Grinding(
    
    class_iri='https://w3id.org/emmo#EMMO_2138677c_845a_4bc2_8be7_7b0a07b4777d',
    
    class_name='Grinding',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2138677c_845a_4bc2_8be7_7b0a07b4777d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Grinding',
        alias="class_name"
    )
    

    
    

    

    