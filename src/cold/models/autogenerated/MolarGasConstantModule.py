
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIExactConstantModule import SIExactConstant







class MolarGasConstant(SIExactConstant):
    """
    Class representing the `MolarGasConstant` entity, which inherits from:
    - SIExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ad6c76cf_b400_423e_820f_cf0c4e77f455'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MolarGasConstant'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MolarGasConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_ad6c76cf_b400_423e_820f_cf0c4e77f455',
    
    class_name='MolarGasConstant',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ad6c76cf_b400_423e_820f_cf0c4e77f455',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MolarGasConstant',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    