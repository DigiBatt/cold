
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HolisticSystemModule import HolisticSystem







class Network(HolisticSystem):
    """
    Class representing the `Network` entity, which inherits from:
    - HolisticSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f93fe78b_9646_4a15_b88b_1c93686a764d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Network'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Network(
    
    class_iri='https://w3id.org/emmo#EMMO_f93fe78b_9646_4a15_b88b_1c93686a764d',
    
    class_name='Network',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f93fe78b_9646_4a15_b88b_1c93686a764d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Network',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    