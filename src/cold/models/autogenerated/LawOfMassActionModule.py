
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalLawModule import PhysicalLaw







class LawOfMassAction(PhysicalLaw):
    """
    Class representing the `LawOfMassAction` entity, which inherits from:
    - PhysicalLaw

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5a7a3028_db9e_4045_ab68_054c6afc91fc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LawOfMassAction'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LawOfMassAction(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5a7a3028_db9e_4045_ab68_054c6afc91fc',
    
    class_name='LawOfMassAction',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5a7a3028_db9e_4045_ab68_054c6afc91fc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LawOfMassAction',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    