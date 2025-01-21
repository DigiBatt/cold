
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalDeviceModule import ElectrochemicalDevice







class ConductivityCell(ElectrochemicalDevice):
    """
    Class representing the `ConductivityCell` entity, which inherits from:
    - ElectrochemicalDevice

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b525a629_a679_464f_bc5b_b49d2fc82686'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConductivityCell'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConductivityCell(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b525a629_a679_464f_bc5b_b49d2fc82686',
    
    class_name='ConductivityCell',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b525a629_a679_464f_bc5b_b49d2fc82686',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConductivityCell',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    