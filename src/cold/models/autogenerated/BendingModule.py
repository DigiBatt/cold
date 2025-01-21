
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingJoinModule import FormingJoin



from .FlexuralFormingModule import FlexuralForming







class Bending(FormingJoin, FlexuralForming):
    """
    Class representing the `Bending` entity, which inherits from:
    - FormingJoin, FlexuralForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_68ee441e_c89e_4391_93c3_e68fef59fe14'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Bending'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Bending(
    
    class_iri='https://w3id.org/emmo#EMMO_68ee441e_c89e_4391_93c3_e68fef59fe14',
    
    class_name='Bending',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_68ee441e_c89e_4391_93c3_e68fef59fe14',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Bending',
        alias="class_name"
    )
    

    
    

    

    