
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineElectrolyteModule import AlkalineElectrolyte







class PotassiumHydroxideSolution(AlkalineElectrolyte):
    """
    Class representing the `PotassiumHydroxideSolution` entity, which inherits from:
    - AlkalineElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_26a0dc36_8171_4a84_88dd_0f5dd7cb2d20'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PotassiumHydroxideSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PotassiumHydroxideSolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_26a0dc36_8171_4a84_88dd_0f5dd7cb2d20',
    
    class_name='PotassiumHydroxideSolution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_26a0dc36_8171_4a84_88dd_0f5dd7cb2d20',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PotassiumHydroxideSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    