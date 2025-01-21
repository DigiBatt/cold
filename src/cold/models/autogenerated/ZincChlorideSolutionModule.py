
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NearNeutralElectrolyteModule import NearNeutralElectrolyte







class ZincChlorideSolution(NearNeutralElectrolyte):
    """
    Class representing the `ZincChlorideSolution` entity, which inherits from:
    - NearNeutralElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7393f12f_e3b9_42d6_bffb_e5613f53108f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincChlorideSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincChlorideSolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7393f12f_e3b9_42d6_bffb_e5613f53108f',
    
    class_name='ZincChlorideSolution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7393f12f_e3b9_42d6_bffb_e5613f53108f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincChlorideSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    