
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReactionRateConstantModule import ReactionRateConstant







class PositiveElectrodeReactionRateConstant(ReactionRateConstant):
    """
    Class representing the `PositiveElectrodeReactionRateConstant` entity, which inherits from:
    - ReactionRateConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_404126e0_cb1b_44e4_98dc_2474185767a1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PositiveElectrodeReactionRateConstant'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PositiveElectrodeReactionRateConstant(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_404126e0_cb1b_44e4_98dc_2474185767a1',
    
    class_name='PositiveElectrodeReactionRateConstant',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_404126e0_cb1b_44e4_98dc_2474185767a1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PositiveElectrodeReactionRateConstant',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    