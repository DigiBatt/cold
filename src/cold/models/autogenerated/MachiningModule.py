
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DefinedEdgeCuttingModule import DefinedEdgeCutting







class Machining(DefinedEdgeCutting):
    """
    Class representing the `Machining` entity, which inherits from:
    - DefinedEdgeCutting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_bfce8136_8f58_4ea5_ab3a_1734170c5d92'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Machining'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Machining(
    
    class_iri='https://w3id.org/emmo#EMMO_bfce8136_8f58_4ea5_ab3a_1734170c5d92',
    
    class_name='Machining',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_bfce8136_8f58_4ea5_ab3a_1734170c5d92',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Machining',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    