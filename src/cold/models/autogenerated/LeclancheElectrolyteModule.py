
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NearNeutralElectrolyteModule import NearNeutralElectrolyte







class LeclancheElectrolyte(NearNeutralElectrolyte):
    """
    Class representing the `LeclancheElectrolyte` entity, which inherits from:
    - NearNeutralElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_23b30468_be7b_45a9_bc11_a8219bc3ab8b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LeclancheElectrolyte'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LeclancheElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_23b30468_be7b_45a9_bc11_a8219bc3ab8b',
    
    class_name='LeclancheElectrolyte',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_23b30468_be7b_45a9_bc11_a8219bc3ab8b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LeclancheElectrolyte',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    