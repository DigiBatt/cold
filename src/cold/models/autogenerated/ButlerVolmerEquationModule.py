
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalRelationModule import ElectrochemicalRelation







class ButlerVolmerEquation(ElectrochemicalRelation):
    """
    Class representing the `ButlerVolmerEquation` entity, which inherits from:
    - ElectrochemicalRelation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d48ea516_5cac_4f86_bc88_21b6276c0938'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ButlerVolmerEquation'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
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
    obj = ButlerVolmerEquation(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d48ea516_5cac_4f86_bc88_21b6276c0938',
    
    class_name='ButlerVolmerEquation',
    
    wikidataReference="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d48ea516_5cac_4f86_bc88_21b6276c0938',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ButlerVolmerEquation',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
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
    

    
    

    

    