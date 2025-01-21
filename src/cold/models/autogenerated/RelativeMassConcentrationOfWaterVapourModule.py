
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity



from .RatioQuantityModule import RatioQuantity







class RelativeMassConcentrationOfWaterVapour(ThermodynamicalQuantity, RatioQuantity):
    """
    Class representing the `RelativeMassConcentrationOfWaterVapour` entity, which inherits from:
    - ThermodynamicalQuantity, RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c106f318_38b1_4261_94cc_f4ac6ccc47af'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RelativeMassConcentrationOfWaterVapour'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RelativeMassConcentrationOfWaterVapour(
    
    class_iri='https://w3id.org/emmo#EMMO_c106f318_38b1_4261_94cc_f4ac6ccc47af',
    
    class_name='RelativeMassConcentrationOfWaterVapour',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c106f318_38b1_4261_94cc_f4ac6ccc47af',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RelativeMassConcentrationOfWaterVapour',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    