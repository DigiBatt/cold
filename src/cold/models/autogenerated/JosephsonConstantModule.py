
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIExactConstantModule import SIExactConstant







class JosephsonConstant(SIExactConstant):
    """
    Class representing the `JosephsonConstant` entity, which inherits from:
    - SIExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ba380bc6_2bfd_4f11_94c7_b3cbaafd1631'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'JosephsonConstant'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = JosephsonConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_ba380bc6_2bfd_4f11_94c7_b3cbaafd1631',
    
    class_name='JosephsonConstant',
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ba380bc6_2bfd_4f11_94c7_b3cbaafd1631',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'JosephsonConstant',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    