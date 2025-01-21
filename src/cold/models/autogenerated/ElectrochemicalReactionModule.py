
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon



from .ChemicalReactionModule import ChemicalReaction







class ElectrochemicalReaction(ElectrochemicalPhenomenon, ChemicalReaction):
    """
    Class representing the `ElectrochemicalReaction` entity, which inherits from:
    - ElectrochemicalPhenomenon, ChemicalReaction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a6a69e90_06b5_45b1_83cf_7c0bf39b2914'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalReaction'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalReaction(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a6a69e90_06b5_45b1_83cf_7c0bf39b2914',
    
    class_name='ElectrochemicalReaction',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a6a69e90_06b5_45b1_83cf_7c0bf39b2914',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalReaction',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    