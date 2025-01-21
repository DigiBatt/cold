
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineElectrolyteModule import AlkalineElectrolyte







class LithiumHydroxideSolution(AlkalineElectrolyte):
    """
    Class representing the `LithiumHydroxideSolution` entity, which inherits from:
    - AlkalineElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e84e691a_df58_465c_9771_7a7fe2212ed5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumHydroxideSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumHydroxideSolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e84e691a_df58_465c_9771_7a7fe2212ed5',
    
    class_name='LithiumHydroxideSolution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e84e691a_df58_465c_9771_7a7fe2212ed5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumHydroxideSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    