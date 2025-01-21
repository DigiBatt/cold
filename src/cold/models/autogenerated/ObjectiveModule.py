
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CodedModule import Coded







class Objective(Coded):
    """
    Class representing the `Objective` entity, which inherits from:
    - Coded

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2a888cdf_ec4a_4ec5_af1c_0343372fc978'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Objective'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Objective(
    
    class_iri='https://w3id.org/emmo#EMMO_2a888cdf_ec4a_4ec5_af1c_0343372fc978',
    
    class_name='Objective',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2a888cdf_ec4a_4ec5_af1c_0343372fc978',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Objective',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    