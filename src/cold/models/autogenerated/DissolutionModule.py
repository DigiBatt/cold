
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalReactionModule import ChemicalReaction







class Dissolution(ChemicalReaction):
    """
    Class representing the `Dissolution` entity, which inherits from:
    - ChemicalReaction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_49263a32_eca6_4644_8144_0d3b14c26d0a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Dissolution'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Dissolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_49263a32_eca6_4644_8144_0d3b14c26d0a',
    
    class_name='Dissolution',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_49263a32_eca6_4644_8144_0d3b14c26d0a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Dissolution',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    