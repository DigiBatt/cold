
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpeedModule import Speed



from .SIExactConstantModule import SIExactConstant







class SpeedOfLightInVacuum(Speed, SIExactConstant):
    """
    Class representing the `SpeedOfLightInVacuum` entity, which inherits from:
    - Speed, SIExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_99296e55_53f7_4333_9e06_760ad175a1b9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpeedOfLightInVacuum'`
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
    obj = SpeedOfLightInVacuum(
    
    class_iri='https://w3id.org/emmo#EMMO_99296e55_53f7_4333_9e06_760ad175a1b9',
    
    class_name='SpeedOfLightInVacuum',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_99296e55_53f7_4333_9e06_760ad175a1b9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpeedOfLightInVacuum',
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
    

    
    

    

    