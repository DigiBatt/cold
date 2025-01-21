
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReferenceElectrodeModule import ReferenceElectrode







class ReversibleHydrogenElectrode(ReferenceElectrode):
    """
    Class representing the `ReversibleHydrogenElectrode` entity, which inherits from:
    - ReferenceElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d9ba00d_04bc_4bdc_85af_3380694f6f68'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReversibleHydrogenElectrode'`
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
    obj = ReversibleHydrogenElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d9ba00d_04bc_4bdc_85af_3380694f6f68',
    
    class_name='ReversibleHydrogenElectrode',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d9ba00d_04bc_4bdc_85af_3380694f6f68',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReversibleHydrogenElectrode',
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
    

    
    

    

    