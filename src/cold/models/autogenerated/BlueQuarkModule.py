
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuarkModule import Quark







class BlueQuark(Quark):
    """
    Class representing the `BlueQuark` entity, which inherits from:
    - Quark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dcca141c_dba1_4f83_86ac_f4cb2d9a1bdd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_dcca141c_dba1_4f83_86ac_f4cb2d9a1bdd',
    
    class_name='BlueQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dcca141c_dba1_4f83_86ac_f4cb2d9a1bdd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueQuark',
        alias="class_name"
    )
    

    
    

    

    