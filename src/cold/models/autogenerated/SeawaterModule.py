
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NearNeutralElectrolyteModule import NearNeutralElectrolyte







class Seawater(NearNeutralElectrolyte):
    """
    Class representing the `Seawater` entity, which inherits from:
    - NearNeutralElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1c0c8f43_7349_4646_94e3_c36727c5c2e3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Seawater'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Seawater(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1c0c8f43_7349_4646_94e3_c36727c5c2e3',
    
    class_name='Seawater',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1c0c8f43_7349_4646_94e3_c36727c5c2e3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Seawater',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    