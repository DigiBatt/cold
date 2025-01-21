
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EntropyModule import Entropy



from .SIExactConstantModule import SIExactConstant







class BoltzmannConstant(Entropy, SIExactConstant):
    """
    Class representing the `BoltzmannConstant` entity, which inherits from:
    - Entropy, SIExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ffc7735f_c177_46a4_98e9_a54440d29209'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BoltzmannConstant'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BoltzmannConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_ffc7735f_c177_46a4_98e9_a54440d29209',
    
    class_name='BoltzmannConstant',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ffc7735f_c177_46a4_98e9_a54440d29209',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BoltzmannConstant',
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
    

    
    

    

    