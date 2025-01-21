
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolModule import Symbol







class Numeral(Symbol):
    """
    Class representing the `Numeral` entity, which inherits from:
    - Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_74b05aed_66bf_43c8_aa2c_752a9ca8be03'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Numeral'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Numeral(
    
    class_iri='https://w3id.org/emmo#EMMO_74b05aed_66bf_43c8_aa2c_752a9ca8be03',
    
    class_name='Numeral',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_74b05aed_66bf_43c8_aa2c_752a9ca8be03',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Numeral',
        alias="class_name"
    )
    

    
    

    

    