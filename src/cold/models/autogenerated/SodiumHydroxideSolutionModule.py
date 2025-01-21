
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineElectrolyteModule import AlkalineElectrolyte







class SodiumHydroxideSolution(AlkalineElectrolyte):
    """
    Class representing the `SodiumHydroxideSolution` entity, which inherits from:
    - AlkalineElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ebd01982_6b0c_48e7_90ef_7b7342009449'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumHydroxideSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumHydroxideSolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ebd01982_6b0c_48e7_90ef_7b7342009449',
    
    class_name='SodiumHydroxideSolution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ebd01982_6b0c_48e7_90ef_7b7342009449',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumHydroxideSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    