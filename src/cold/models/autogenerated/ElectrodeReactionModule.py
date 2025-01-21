
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalReactionModule import ElectrochemicalReaction







class ElectrodeReaction(ElectrochemicalReaction):
    """
    Class representing the `ElectrodeReaction` entity, which inherits from:
    - ElectrochemicalReaction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2e3e14f9_4cb8_45b2_908e_47eec893dec8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodeReaction'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrodeReaction(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2e3e14f9_4cb8_45b2_908e_47eec893dec8',
    
    class_name='ElectrodeReaction',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2e3e14f9_4cb8_45b2_908e_47eec893dec8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodeReaction',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    