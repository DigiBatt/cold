
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalRelationModule import ElectrochemicalRelation







class NernstEinsteinEquation(ElectrochemicalRelation):
    """
    Class representing the `NernstEinsteinEquation` entity, which inherits from:
    - ElectrochemicalRelation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d7e5fea_a49a_4a19_a8de_8e24c60e420c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NernstEinsteinEquation'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NernstEinsteinEquation(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d7e5fea_a49a_4a19_a8de_8e24c60e420c',
    
    class_name='NernstEinsteinEquation',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d7e5fea_a49a_4a19_a8de_8e24c60e420c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NernstEinsteinEquation',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    